clear; close all
% FOR ALL RAW DATA COLUMNS GO: MAG, ACC, GYRO AND X,Y,Z FOR EACH
data = readmatrix('trans_x.csv');
gyro = data(:,1:3);
acc = data(:,4:6);
mag = data(:,7:9);
dt = 20e-3;
tl = 1:size(data,1);

figure(1)
subplot(3,1,1)
plot(tl,acc(:,1))
xlabel('Time (20*ms)')
ylabel('x')

subplot(3,1,2)
plot(tl,acc(:,2))
xlabel('Time (20*ms)')
ylabel('y')

subplot(3,1,3)
plot(tl,acc(:,3))
xlabel('Time (20*ms)')
ylabel('z')

v = zeros(1,size(data,1));
jerk = v;
v(1) = 0; 

for i = 2:size(data,1)
    v(i) = v(i-1) + acc(i-1,3)*dt;
end

for t = 1:size(data,1)
jerk(t) = -log(((dt^3)/(max(v)^2))*(acc(t,3)*dt));
end
jerk = abs(jerk);

figure(2)
plot(tl,v)
xlabel('Time (20*ms)')
ylabel('z-velocity')

figure(3)
plot(tl,jerk)
xlabel('Time (20*ms)')
ylabel('Smoothness')
