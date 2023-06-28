package com.educandoweb.course.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.educandoweb.course.entities.User;
import com.educandoweb.course.repository.UserRepository;

@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;

    public List<User> listAllUser() {
        return userRepository.findAll();
    }

    public User addUser(User user) {
        return userRepository.save(user);
    }

    public Optional<User> findById(Long id) {
        return userRepository.findById(id);
    }

    public void deleteById(Long id) {
        userRepository.deleteById(id);
    }

    public User update(Long id, User user) {
        User entity = userRepository.getReferenceById(id);
        updateData(entity, user);
        return userRepository.save(entity);
    }

    public void updateData(User entity, User user) {
        entity.setEmail(user.getEmail());
        entity.setPhone(user.getPhone());
        entity.setName(user.getName());
    }
}
